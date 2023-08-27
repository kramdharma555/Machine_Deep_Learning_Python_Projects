from PIL import Image, ImageFilter
image = Image.open('NASA.jpg')
image = image.convert('L') 
image = image.filter(ImageFilter.FIND_EDGES)
image.save(r'ImageFound.jpg')
image.show('ImageFound.jpg')

# from PIL import Image, ImageFilter
  
# img = Image.open(r"NASA.jpg")
  
# # Converting the image to grayscale, as Sobel Operator requires
# # input image to be of mode Grayscale (L)
# img = img.convert("L")
  
# # Calculating Edges using the passed laplican Kernel
# final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
#                                           -1, -1, -1, -1), 1, 0))
  
# final.save("EDGE_sample.png")
# final.show("EDGE_sample.png")
