from PIL import Image
import sys

amoledify = lambda x, threshold: 0 if x < threshold else x


def main(image, threshold):
  img = Image.open(image)
  img = img.convert("RGB")
  img = Image.eval(img, lambda x: amoledify(x, threshold))
  img.save(f'{image.rsplit(".",1)[0]}_amoledified.{image.rsplit(".",1)[1]}')


if __name__ == "__main__":
  if len(sys.argv) >= 2 and len(sys.argv) < 4:
    image = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) == 3 else 10
    main(image, threshold)
  else:
    print("Usage: amoledify.py <Image Path> <Threshold Value(Optional) = 10 >")
