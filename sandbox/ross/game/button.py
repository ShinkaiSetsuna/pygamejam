class Button():

    def __init__(self, pygame, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.mode = 0
        self.thickness = 2
        self.active = False

    def update_text(self, text_sur):
        self.text_surface = text_sur
        self.text_pos = ((self.rect[0]+(self.rect[2]/2)-self.text_surface.get_width()/2), \
        (self.rect[1]+(self.rect[3]/2)-self.text_surface.get_height()/2))
    def handle_event(self, pygame, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.rect.collidepoint(event.pos):
                self.mode = 2
                print("Boop.")

    def hover_check(self, mouse_pos):
        self.mode = 1 if self.rect.collidepoint(mouse_pos) else 0

    def draw(self, pygame, sur, ic=(15,15,255), hc=(255,0,255), ac=(0,255,255)):
        if self.mode == 0: color = ic
        elif self.mode == 1: color = hc
        else: color = ac
        # Blit the rect.
        pygame.draw.rect(sur, color, self.rect, 0)
        # Blit the text.
        sur.blit(self.text_surface, self.text_pos)
