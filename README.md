# SD-latent-mirroring
Applies mirroring and flips to the latent images mid-generation to produce anything from subtle balanced compositions to perfect reflections

## UI

![image](https://user-images.githubusercontent.com/35278260/201224546-0349c073-10d6-47ac-9c94-80314540c398.png)
- Mirror Application Mode
  - **None** - Do not mirror
  - **Alternate Steps** - flip or rotate the latents on each step
  - **Blend Average** - take the average of the original latents and their flipped or rotated version
- Mirror Style
  - **Vertical Mirroring** - Mirror vertically flipping left for right.
  - **Horizontal Mirroring** - Mirror horizontally flipping up for down.
  - **Horizontal+Vertical Mirroring** - flip alternately horizontally and vertically.
  - **90 Degree Rotation** - Rotate 90 degrees clockwise.
  - **180 Degree Rotation** - Rotate 180 degrees
  - **Roll Channels** - Sequentially switch the 'channels' of the latent image for colour variations.
- **Maximum steps fraction to mirror at** - a decimal percentage representing the maximum step to apply the mirroring on, 0.5 = 50%, stopping at the 10th step out of 20 when 20 steps are used.

## Outputs

Vertical Mirroring:

![image](https://user-images.githubusercontent.com/35278260/199627861-07b2c1a6-0271-4505-814d-01ad31a68f79.png)

Horizontal Mirroring:

![image](https://user-images.githubusercontent.com/35278260/199627881-6f62a227-3a6c-4470-9c18-2ed8bc57194c.png)

90 Degree Rotation:

![image](https://user-images.githubusercontent.com/35278260/199627897-bdef0e03-3230-4b1d-ba21-0e2f15bf14e7.png)

180 Degree Rotation:

![image](https://user-images.githubusercontent.com/35278260/199627888-8b778a8a-d053-456f-8651-323b01126d87.png)

Higher `Maximum steps fraction to mirror at` values producer stronger symetries:

![image](https://user-images.githubusercontent.com/35278260/199627949-0529921f-8c82-4d01-b3cb-23b91d68bc9c.png)
