import time

STATIONS = [360, 720, 1080, 1440, 1800]


class Train:

    def __init__(self):
        
        self.distance = 0

    def move(self):

        time.sleep(1)
        self.distance += 1
        print(f'demo_train distance: {self.distance}')



class Track:

    distance = 1800 # km


def start_simulation():

    demo_train = Train()
    line1 = Track()
    
    while demo_train.distance < line1.distance:
        demo_train.move()
        if demo_train.distance in STATIONS:
            print(f'demo_train passed station {demo_train.distance}')
    
    print(f'demo_train stop at {demo_train.distance}')



start_simulation()


