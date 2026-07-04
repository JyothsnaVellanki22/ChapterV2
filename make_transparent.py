import collections
from PIL import Image

def make_bg_transparent(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    visited = set()
    queue = collections.deque()
    
    # Add all border pixels to queue
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(1, height - 1):
        queue.append((0, y))
        queue.append((width - 1, y))
        
    def is_white(color):
        r, g, b, a = color
        # allow some tolerance
        return r > 240 and g > 240 and b > 240
        
    while queue:
        x, y = queue.popleft()
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        
        if is_white(pixels[x, y]):
            # make transparent
            pixels[x, y] = (255, 255, 255, 0)
            
            if x + 1 < width: queue.append((x+1, y))
            if x - 1 >= 0: queue.append((x-1, y))
            if y + 1 < height: queue.append((x, y+1))
            if y - 1 >= 0: queue.append((x, y-1))

    img.save(out_path)
    print("Saved transparent logo.")

make_bg_transparent('assets/logo.png', 'assets/logo_transparent.png')
