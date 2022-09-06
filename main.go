package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	if len(os.Args) != 3 {

	} else {
		dimentions, err := strconv.Atoi(os.Args[1])
		if err == nil {
			var minT, maxT, minL, maxL int
			switch os.Args[2] {
			case "D":
				minT = dimentions / 6
				maxT = dimentions + int(float64(dimentions)*9)
				maxL = minT + 3
				minL = maxL / 3
			case "R":
				minT = dimentions - dimentions/2
				maxT = dimentions + int(float64(dimentions)*1.4)
				maxL = dimentions / 4
				minL = maxL / 3
			case "S":
				minT = 1
				maxT = dimentions / 2
				maxL = dimentions / 2
				minL = maxL / 3
			}
			/*
				fmt.Println(minT)
				fmt.Println(maxT)
				fmt.Println(maxL)
				fmt.Println(minL)
				fmt.Println(dimentions)
			*/
			mapa := createMap(dimentions, maxT, minT, maxL, minL)
			//drawMap(mapa, dimentions)
			expMap(mapa, dimentions)
		}

	}
	//drawMap(createMap(50, 80, 20, 20, 3), 50)
}

func createMap(dimentions int, maxTunnels int, minTunnels int, maxLength int, minLenght int) [][]int {

	mapa := createArray(dimentions)

	rand.Seed(time.Now().UnixMilli())
	row := rand.Intn(dimentions)
	column := rand.Intn(dimentions)

	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	var lastDirection [2]int
	var randomDirection [2]int

	for maxTunnels > minTunnels && maxLength > 0 && dimentions > 0 {

		r := rand.Intn(4)
		randomDirection[0], randomDirection[1] = directions[r][0], directions[r][1]
		for randomDirection == lastDirection {
			r = rand.Intn(4)
			randomDirection[0], randomDirection[1] = directions[r][0], directions[r][1]
		}

		randomLength := rand.Intn(maxLength-minLenght) + minLenght
		tunnelLength := 0
		for tunnelLength < randomLength {
			if ((row == 0) && (randomDirection[0] == -1)) ||
				((column == 0) && (randomDirection[1] == -1)) ||
				((row == dimentions-1) && (randomDirection[0] == 1)) ||
				((column == dimentions-1) && randomDirection[1] == 1) {
				break
			} else {
				mapa[row][column] = 1
				row += randomDirection[0]
				column += randomDirection[1]
				tunnelLength++
			}
		}

		if tunnelLength > 0 {
			lastDirection = randomDirection
			maxTunnels--
		}
	}

	return mapa
}

func createArray(dimentions int) [][]int {
	mapa := make([][]int, dimentions)
	for i := 0; i < dimentions; i++ {
		mapa[i] = make([]int, dimentions)
	}

	for i := 0; i < dimentions; i++ {
		for j := 0; j < dimentions; j++ {
			mapa[j][i] = 0
		}
	}

	return mapa

}

func expMap(mapa [][]int, dimentions int) {
	for i := 0; i < dimentions; i++ {
		for j := 0; j < dimentions; j++ {
			fmt.Print(mapa[j][i])
			fmt.Print(" ")
		}
		fmt.Println("")
	}
}

func drawMap(mapa [][]int, dimentions int) {
	for i := 0; i < dimentions; i++ {
		for j := 0; j < dimentions; j++ {
			if mapa[j][i] == 1 {
				fmt.Print(tunnel())
			} else if mapa[j][i] == 2 {
				fmt.Print(wall())
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println("")
	}
	fmt.Print("\u001b[0m")
}

func tunnel() string {
	return "\u001b[44;1m\u001b[34;1mt\u001b[30m\u001b[40m"
}

func wall() string {
	return "\u001b[43;1m\u001b[33;1mt\u001b[30m\u001b[40m"
}
