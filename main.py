import pyautogui
import keyboard
import time

backroundColourRGB = (40, 38, 40)
revolutionsCoordinates: dict[str, tuple[int, int]] = {
	'Red Ascension': (334, 240),
	'Orange Ascension': (334, 320),
	'Yellow Ascension': (334, 400),
	'Green Ascension': (334, 480),
	'Turquoise Ascension': (334, 560),
	'Cyan Ascension': (334, 640),
	'Blue Ascension': (334, 720),
	'Purple Ascension': (334, 800),
	'Pink Ascension': (334, 880),
	'White Ascension': (334, 960),
}
currentRevolutionsCoordinates: dict[str, tuple[int, int]] = {
	'Red Ascension': (334, 240),
	'Orange Ascension': (334, 320),
}
revolutionsDictionary: dict[int, str] = {
	0: 'Red Ascension',
	1: 'Orange Ascension',
	2: 'Yellow Ascension',
	3: 'Green Ascension',
	4: 'Turquoise Ascension',
	5: 'Cyan Ascension',
	6: 'Blue Ascension',
	7: 'Purple Ascension',
	8: 'Pink Ascension',
	9: 'White Ascension',
}

def main() -> None:

	botloop()


def botloop() -> None:

	buyRevolutions()


def buyRevolutions() -> None:

	while True:
		checkRevolutions()
		for Coordinates in currentRevolutionsCoordinates.values():
			if keyboard.is_pressed('space'):
				break
			if not pyautogui.pixelMatchesColor(Coordinates[0], Coordinates[1], backroundColourRGB):
				pyautogui.click(Coordinates[0], Coordinates[1])


def checkRevolutions() -> None:
	while True:
		pairs: int = len(currentRevolutionsCoordinates) - 1
		check: int = pairs + 1
		dictionaryKey: str = revolutionsDictionary[check]
		if not pyautogui.pixelMatchesColor(revolutionsCoordinates[dictionaryKey][0],revolutionsCoordinates[dictionaryKey][1], backroundColourRGB):
			currentRevolutionsCoordinates[dictionaryKey] = (revolutionsCoordinates[dictionaryKey][0],revolutionsCoordinates[dictionaryKey][1])
			continue
		else:
			break


def printMouseCoordsonSpacePress() -> None:

	while True:
		if keyboard.is_pressed('space'):
			print(pyautogui.position())
			time.sleep(0.2)


if __name__ == '__main__':

	time.sleep(2)
	main()



