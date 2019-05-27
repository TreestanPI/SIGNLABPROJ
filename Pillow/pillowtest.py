from PIL import Image, ImageFilter, ImageEnhance

def main():
    #print('\n\n*****\t\t\t\t\t*****\tImage Filtering\t*****\t\t\t\t\t*****\n')
    while(True):
        print('Enter filename:')
        srcFile = input()
        if srcFile == 'Exit':
            break
        elif srcFile is not None:
            im = Image.open(srcFile)
            im.show()
            imList = []
            imList.append(im)
            filterLoop = True
            while(filterLoop):
                print('\nAvailable filters')
                print('1. Contrast')
                print('2. Color')
                print('3. Brightness')
                print('4. Sharpness')
                print('5. Blur')
                print('0. Done')
                filterChoice = int(input('\nSelect number for the chosen filter: '))
                factorLoop = True
                while(factorLoop):
                        if filterChoice is 1:
                            print('***\nNote that the original image factor is 1')
                            factor = float(input('Select Factor from 0.5 - 10: '))
                            if 0 <= factor <= 10:
                                imList.append(ImageEnhance.Contrast(imList[-1]).enhance(factor))
                                factorLoop = not factorLoop
                                print('Contrast changed by ', (factor - 1) * 100, "%")
                                imList[-1].show()
                        elif filterChoice is 2:
                            print('***\nNote that the original factor is 1 ***')
                            factor = float(input('Select Factor from 0.5 - 10: '))
                            if 0 <= factor <= 10:
                                imList.append(ImageEnhance.Color(imList[-1]).enhance(factor))
                                factorLoop = not factorLoop
                                print('Color changed by ', (factor - 1) * 100, "%")
                                imList[-1].show()
                        elif filterChoice is 3:
                            print('***\nNote that the original factor is 1 ***')
                            factor = float(input('Select Factor from 0.5 - 10: '))
                            if 0 <= factor <= 10:
                                imList.append(ImageEnhance.Brightness(imList[-1]).enhance(factor))
                                factorLoop = not factorLoop
                                print('Brightness changed by ', (factor - 1 * 100, "%"))
                                imList[-1].show()
                        elif filterChoice is 4:
                            print('***\nNote that the original factor is 1 ***')
                            factor = float(input('Select Factor from 0.5 - 10: '))                            
                            if 0 <= factor <= 10:
                                imList.append(ImageEnhance.Sharpness(imList[-1]).enhance(factor))
                                factorLoop = not factorLoop
                                print('Sharpness changed by ', (factor - 1) * 100, "%")
                                imList[-1].show()
                        elif filterChoice is 5:
                            print('***\nNote that the original factor is 1 ***')
                            factor = float(input('Select Factor from 0.5 - 10: '))
                            if 0 <= factor <= 10:
                                imList.append(imList[-1].filter(ImageFilter.GaussianBlur))
                                factorLoop = not factorLoop
                                print('Blur changed by ', (factor - 1) * 100, "%")                            
                                imList[-1].show() 
                        elif filterChoice is 0:   
                            print('Thank you for using this image filter.')
                            exit()
                        else:
                            print('Invalid input. Please try again.')
                            break

if __name__ == '__main__':
    main()