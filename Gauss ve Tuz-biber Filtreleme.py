import cv2
import numpy as np
import matplotlib as plt




def tuz_biber_gurultu_ekleme(image, salt_prob=0.02, pepper_prob=0.02):
    gurultu = np.copy(image)
    total_pixels = image.shape[0] * image.shape[1]

    # Salt (beyaz) pikseller
    num_salt = int(total_pixels * salt_prob)
    coords = [np.random.randint(0, i, num_salt) for i in image.shape[:2]]
    gurultu[coords[0], coords[1]] = 255

    # Pepper (siyah) pikseller
    num_pepper = int(total_pixels * pepper_prob)
    coords = [np.random.randint(0, i, num_pepper) for i in image.shape[:2]]
    gurultu[coords[0], coords[1]] = 0

    return gurultu



def gauss_gurultu_ekleme(image, mean=0, sigma=25):
    gauss = np.random.normal(mean, sigma, image.shape).astype('float32')
    gurultu = np.clip(image + gauss, 0, 255).astype('uint8')
    return gurultu

def cift_katmanlı_hibrid_filtreleme(image):
    ilk_katman=cv2.medianBlur(image,3)
    cv2.imshow("Ilk katman",ilk_katman)

    ikinci_katman=cv2.GaussianBlur(ilk_katman,(5,5),1)

    return cv2.imshow("Ikinci katman",ikinci_katman)


def cift_katmanlı_hibrid_filtreleme_katmanlari_degistir(image):
    ilk_katman=cv2.GaussianBlur(image,(5,5),1)
    cv2.imshow("Ilk katman gauss filter uygulanırsa",ilk_katman)

    ikinci_katman=cv2.medianBlur(ilk_katman,3)
    return cv2.imshow("Ikinci katman medyan filter uygulanırsa",ikinci_katman)


imagine = cv2.imread('aksaray.jpg',1)

if imagine is not None:
    # görüntüyü yeniden boyutlandırmaya yarar
    imagine2 = cv2.resize(imagine, (800, 640))
    cv2.imshow("Orjinal", imagine2)

    #resime gauss gürültüsü ekler
    gausslu_resim =gauss_gurultu_ekleme(imagine2)
    cv2.imshow("Gausslu resim",gausslu_resim)

    #gauss filtresi sayesinde gauss gürültüsünü filtreler 
    gauss_filtresi = cv2.GaussianBlur(gausslu_resim,(5,5),1)
    cv2.imshow("Gauss filtresi",gauss_filtresi)


    #resime tuz-biber eklemeye yarar
    tuz_biber_resim = tuz_biber_gurultu_ekleme(imagine2)
    cv2.imshow("Tuz-Biberli resim",tuz_biber_resim)

    #ortalama filtresi sayesinde tuz-biber gürültüsünü filtreler 
    medyan_filtresi = cv2.medianBlur(tuz_biber_resim,3)
    cv2.imshow("Medyan filtresi",medyan_filtresi)

    #tuz-biber gürültüsü ekleyen fonksiyona gauss gürültülü resim göndermeye yarar
    gurultu_karısımı = tuz_biber_gurultu_ekleme(gauss_gurultu_ekleme(imagine2))
    cv2.imshow("Tuz-Biber Ve Gauss",gurultu_karısımı)

    gurultu_karısımı_filtreleme=cift_katmanlı_hibrid_filtreleme(gurultu_karısımı)
    gurultu_karısımı_filtreleme=cift_katmanlı_hibrid_filtreleme_katmanlari_degistir(gurultu_karısımı)

    key=cv2.waitKey()
    if key ==ord("q"):
        quit() 
else:
    print("the imagine not downloaded.Please check your file path or file name...")


  
