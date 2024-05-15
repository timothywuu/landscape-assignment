import pygame
import math
pygame.init()

#==========================================================================================================================#

### SET-UP DISPLAY ###
WIDTH = 1440
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#==========================================================================================================================#

### GLOBAL VARIABLES ###
FPS = 60
clock = pygame.time.Clock()

# clouds
cloud_x = 200
cloud_y = 300
cloud_x2 = cloud_x - 600
cloud_y2 = cloud_y - 125
cloud_x3 = cloud_x + 500
cloud_y3 = cloud_y - 100

cloud_normal_radius = 35
cloud_large_radius = cloud_normal_radius + 5

cloud_colour = (255, 255, 255)

# sun
sun_radius = 100
sun_x = 415
sun_x2 = sun_x
sun_y = 700
sun_y2 = sun_y

# moon
moon_radius = 70
moon_x = sun_x2
moon_y = sun_y2

# boat
hull_x = 650
hull_y = 680
hull_width = 400
hull_height = 55

wave_height = 0.6
wave_frenquency = 2.5

# day/nights cycle
is_day = True
day_colour = (165, 250, 255)
night_colour = (45, 40, 70)

#==========================================================================================================================#

### GAME LOOP ###
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#==========================================================================================================================#

### GAME STATUS UPDATES ###

    # background colour
    current_color = day_colour if is_day else night_colour
    screen.fill(current_color)

    # clouds
    pygame.draw.circle(screen, cloud_colour, (cloud_x3, cloud_y3), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x3 + 50, cloud_y3 + 3 ), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x3 + 100, cloud_y3), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x3 + 30, cloud_y3 - 25), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x3 + 75 , cloud_y3 - 30), cloud_large_radius)

    if cloud_x >= WIDTH:
        cloud_x = -(cloud_large_radius * 5)
    cloud_x += 1

    pygame.draw.circle(screen, cloud_colour, (cloud_x, cloud_y), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 50, cloud_y + 3), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 100, cloud_y), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 30, cloud_y - 25), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 75, cloud_y - 30), cloud_large_radius)

    if cloud_x2 >= WIDTH:
        cloud_x2 = -(cloud_large_radius * 5)
    cloud_x2 += 1

    pygame.draw.circle(screen, cloud_colour, (cloud_x2, cloud_y2), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x2 + 50, cloud_y2 + 3 ), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x2 + 100, cloud_y2), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x2 + 30, cloud_y2 - 25), cloud_normal_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud_x2 + 75 , cloud_y2 - 30), cloud_large_radius)

    if cloud_x3 >= WIDTH:
        cloud_x3 = -(cloud_large_radius * 5)
    cloud_x3 += 1


    # sun and moon
    if is_day:
        pygame.draw.circle(screen, (255, 255, 0), (sun_x, sun_y), sun_radius)
        sun_y -= 2
        sun_x += 0.5
        if sun_y <= 0 - sun_radius:
            is_day = False
            moon_x = sun_x2
            moon_y = sun_y2 
        else:
            is_day = True
    else:
        pygame.draw.circle(screen, (210, 215, 220), (moon_x, moon_y), moon_radius)
        pygame.draw.circle(screen, (140, 145, 150), (moon_x - (moon_radius/4), moon_y - (moon_radius/2.5)), moon_radius/5)
        pygame.draw.circle(screen, (140, 145, 150), (moon_x - (moon_radius/2), moon_y - (moon_radius/15)), moon_radius/6)
        pygame.draw.circle(screen, (140, 145, 150), (moon_x + (moon_radius/2.75), moon_y + (moon_radius/3)), moon_radius/3)
        moon_y -= 2
        moon_x += 0.5
        if moon_y <= 0 - moon_radius:
            is_day = True
            sun_x = sun_x2
            sun_y = sun_y2
        else:
            is_day = False


    # hills
    pygame.draw.polygon(screen, (30, 220, 45), [[0, 50], [640, HEIGHT], [0, HEIGHT]]) #left hill
    pygame.draw.polygon(screen, (95, 240, 60), [[0, HEIGHT - 50], [1440, HEIGHT], [WIDTH, 150]]) #top hill
    pygame.draw.polygon(screen, (25, 225, 55), [[0, HEIGHT - 50], [1440, HEIGHT], [WIDTH, 400]]) #middle hill
    pygame.draw.polygon(screen, (15, 200, 40), [[0, HEIGHT - 50], [1440, HEIGHT], [WIDTH, 625]]) #bottom hill


    # water
    water_x = 0
    water_y = 700
    pygame.draw.rect(screen, (65, 225, 245), [0, 705, 1440, 300], 0)


    # boat
    mast_x = hull_x + (hull_width - hull_width * (7/10))
    mast_y = hull_y - 325
    mast_width = (hull_width/12) + 1
    mast_height = (hull_y - mast_y) + 1

    sail_x = mast_x + mast_width
    sail_y = mast_y
    sail_width = hull_x + hull_width * (4/5)
    sail_height = sail_y + abs(mast_height - (mast_height/6))

    pygame.draw.rect(screen, (230, 55, 55), [hull_x, hull_y, hull_width, hull_height], 0, 50) #hull
    pygame.draw.rect(screen, (110, 65, 30), [mast_x, mast_y, mast_width, mast_height], 0,) #mast
    pygame.draw.polygon(screen, (255, 255, 255), [[sail_x, sail_y], [sail_x, sail_height], [sail_width, sail_height]]) #sail

    if hull_x >= WIDTH:
        hull_x = -(hull_width + (hull_width * (1/3)))
    hull_x += 1

    time_in_seconds = pygame.time.get_ticks() / 1000
    wave_offset = math.sin(time_in_seconds * 2 * math.pi / wave_frenquency) * wave_height
    hull_y = hull_y + wave_offset

#==========================================================================================================================#
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
