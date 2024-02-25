import pygame,sys,os 

class Video:
 
    def __init__(self, path):
        self.path = self.convert_os_path_to_win(path)
        self.path = self.path + "\\images"

        try:
            os.mkdir(self.path)
            print("folder '{}' created ".format(self.path))
        except FileExistsError:
            print("folder {} already exists".format(self.path))

        self.name = "capture"
        self.cnt = 0
 
        # Ensure we have somewhere for the frames
        try:
            os.makedirs(self.path)
        except OSError:
            pass
    
    def make_png(self,screen):
        self.cnt+=1
        fullpath = self.path + "\\"+self.name + "%08d.png"%self.cnt
        pygame.image.save(screen,fullpath)
 
    def make_mp4(self):
        pth = self.path + "\\capture%08d.png"
        vid_path = f"ffmpeg -r 200 -i {pth} -vcodec mpeg4 -q:v 0 -y movie.mp4"
        os.system(vid_path)
 
    def convert_os_path_to_win(self, path: str) -> str:
            pth = str(path)       
            ind = pth.find("\\")
            indices = [ind]
            for i in range(1, len(pth)):
                ind = pth.find("\\", ind + 1)
                if -1 != ind: 
                    indices.append(ind)  
                else:
                    break 

            windows_pth = pth
            for i, index in enumerate(indices):
                windows_pth = windows_pth[:index+i]+"\\"+windows_pth[index+i:]

            return windows_pth

 
if __name__  == '__main__':
    video = Video(os.getcwd())
    video.make_mp4()