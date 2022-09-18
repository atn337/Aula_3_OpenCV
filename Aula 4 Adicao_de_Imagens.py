import cv2

Image1 = cv2.imread("C:\\Users\Anatan P. B. Santos\\source\\repos\\Aula_3_OpenCV\\astronauta0.png")
cv2.waitKey(0)
cv2.destroyAllWindows()
Image2 = cv2.imread("C:\\Users\Anatan P. B. Santos\\source\\repos\\Aula_3_OpenCV\\espaco4.png")
cv2.waitKey(0)
cv2.destroyAllWindows()


Image1_add_Image2 = cv2.add(Image1, Image2)
cv2.imwrite('C:\\Users\Anatan P. B. Santos\\source\\repos\\Aula_3_OpenCV\\astronauta0.png', Image1_add_Image2 )
cv2.imshow('C:\\Users\Anatan P. B. Santos\\source\\repos\\Aula_3_OpenCV\\espaco4.png', Image1_add_Image2 )
cv2.waitKey(0)
cv2.destroyAllWindows()