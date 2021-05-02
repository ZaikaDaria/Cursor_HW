from abc import abstractmethod, ABC


class Laptop(ABC):
     @abstractmethod
     def screen(self):
          raise NotImplementedError

     @abstractmethod
     def keyboard(self):
          raise NotImplementedError

     @abstractmethod
     def touchpad(self):
         raise NotImplementedError

     @abstractmethod
     def webcam(self):
         raise NotImplementedError

     @abstractmethod
     def ports(self):
          raise NotImplementedError

     @abstractmethod
     def dynamics(self):
          raise NotImplementedError


class HPLaptop(Laptop):
     def __init__(self, screen_size, keyboard_type, touchpad_type, webcam_type, ports_type, dynamics_type):
          self.screen_size = screen_size
          self.keyboard_type = keyboard_type
          self.touchpad_type = touchpad_type
          self.webcam_type = webcam_type
          self.ports_type = ports_type
          self.dynamics_type = dynamics_type

     def screen(self):
          print(f'Screen size: {self.screen_size}')

     def keyboard(self):
          print(f'Keyboard: {self.keyboard_type}')

     def touchpad(self):
          print(f'Touchpad: {self.touchpad_type}')

     def webcam(self):
          print(f'Web Camera: {self.webcam_type}')

     def ports(self):
          print(f'Ports: {self.ports_type}')

     def dynamics(self):
          print(f'Dynamics: {self.dynamics_type}')

hplaptop = HPLaptop('15.60-inch',
                  'Full-size island-style shadow black RGB backlit keyboard',
                  'Touchpad with multi-touch gesture support ',
                  'HP Wide Vision FHD Camera with integrated dual array digital microphone',
                  'USB 2.0',
                  'Audio by Bang & Olufsen, dual speakers')

hplaptop.screen()
hplaptop.keyboard()
hplaptop.touchpad()
hplaptop.webcam()
hplaptop.ports()
hplaptop.dynamics()
