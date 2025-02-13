import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = True


backroundColourRGB = (40, 38, 40)
lapUpgradeButtonsX = 334
lapUpgradeButtonsY = [240, 320, 400, 480, 560, 640, 720, 800, 880, 960]
lapUpgradeButtonsYReverse = [960, 880, 800, 720, 640, 560, 480, 400, 320, 240]

def main() -> None:
	botloop()

def botloop() -> None:

	while True:
		try:

			for pixel in lapUpgradeButtonsYReverse:
				if keyboard.is_pressed('space'):
					break
				if not pyautogui.pixelMatchesColor(lapUpgradeButtonsX, pixel, backroundColourRGB):
					pyautogui.click(lapUpgradeButtonsX, pixel)
		except KeyboardInterrupt:
			break

def printMouseLocationSpacePress():

	while True:
		if keyboard.is_pressed('space'):
			print(pyautogui.position())
			time.sleep(0.2)


if __name__ == '__main__':

	time.sleep(5)
	main()



