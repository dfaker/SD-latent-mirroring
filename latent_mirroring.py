import torch
import modules.scripts as scripts
import gradio as gr
from modules.script_callbacks import on_cfg_denoiser
from modules import processing


class Script(scripts.Script):
    def title(self):
        return "Latent Mirroring"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        mirror_mode = gr.Radio(label='Mirror application mode', choices=['None', 'Alternate Steps', 'Blend Average'], value='Alternate Steps', type="index")
        mirror_style = gr.Radio(label='Mirror style', choices=['Vertical Mirroring', 'Horizontal Mirroring', '90 Degree Rotation', '180 Degree Rotation'], value='Vertical Mirroring', type="index")
        mirroring_max_step_fraction = gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label='Maximum steps fraction to mirror at', value=0.25)
        self.run_callback = False
        return [mirror_mode, mirror_style, mirroring_max_step_fraction]

    def denoise_callback(self, params):

        if self.run_callback and params.sampling_step < params.total_sampling_steps*self.mirroring_max_step_fraction:
            if self.mirror_mode == 1:
                if self.mirror_style == 0:
                    params.x[:, :, :, :] = torch.flip(params.x, [3])
                elif self.mirror_style == 1:
                    params.x[:, :, :, :] = torch.flip(params.x, [2])
                elif self.mirror_style == 2:
                    params.x[:, :, :, :] = torch.rot90(params.x, dims=[2, 3])
                elif self.mirror_style == 3:
                    params.x[:, :, :, :] = torch.rot90(torch.rot90(params.x, dims=[2, 3]), dims=[2, 3])
            elif self.mirror_mode == 2:
                if self.mirror_style == 0:
                    params.x[:, :, :, :] = (torch.flip(params.x, [3]) + params.x)/2
                elif self.mirror_style == 1:
                    params.x[:, :, :, :] = (torch.flip(params.x, [2]) + params.x)/2
                elif self.mirror_style == 2:
                    params.x[:, :, :, :] = (torch.rot90(params.x, dims=[2, 3]) + params.x)/2
                elif self.mirror_style == 3:
                    params.x[:, :, :, :] = (torch.rot90(torch.rot90(params.x_in, dims=[2, 3]), dims=[2, 3]) + params.x_in)/2

    def run(self, p, mirror_mode, mirror_style, mirroring_max_step_fraction):

        self.mirror_mode = mirror_mode
        self.mirror_style = mirror_style
        self.mirroring_max_step_fraction = mirroring_max_step_fraction

        if not hasattr(self, 'callbacks_added'):
            on_cfg_denoiser(self.denoise_callback)
            self.callbacks_added = True

        self.run_callback = True
        result = processing.process_images(p)
        self.run_callback = False

        return result
