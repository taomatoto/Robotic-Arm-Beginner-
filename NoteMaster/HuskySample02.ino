//start huskylens - get the latest note position - dicision - pass the position to pycharm through serialport
//with music$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
#include "HUSKYLENS.h"
//#include "SoftwareSerial.h" //not use

HUSKYLENS huskylens;
//HUSKYLENS green line >> SDA; blue line >> SCL
void printResult(HUSKYLENSResult result);

// correct position of note (centerX, correctNote)
int correctNote;
int centerX[4];
int centerY[4]; //to be compared with correctNote
bool password = false; //false means the robot does not move

//the message to robot string('targetIndex','targetX','targetY')
int targetY;
int targetX;
int targetIndex;

int checkIndex;

void setup() {
  //setup the huskylens
  Serial.begin(115200);
  Wire.begin();
  while (!huskylens.begin(Wire))
  {
    //    Serial.println(F("Begin failed!"));
    //    Serial.println(F("1.Please recheck the \"Protocol Type\" in HUSKYLENS (General Settings>>Protocol Type>>I2C)"));
    //    Serial.println(F("2.Please recheck the connection."));
    delay(100);
  }
}

void loop() {
  //initialize the huskylens
  if (!huskylens.request()) {} //Serial.println(F("9,9,9"));//Fail to request data from HUSKYLENS
  else if (!huskylens.isLearned()) {} //Serial.println(F("9,9,9"));//Nothing learned
  else if (!huskylens.available()) {} //Serial.println(F("9,9,9"));//No block or arrow appears
  else
  {
    ////////////////////////////////////////////////////////////////////////
    //the dicision is made during this else
    int n = 0; // how many notes on the board
    delay(2000);//to make sure the block is stable
    // the first one usually meets bug, so start from index 1
    while (huskylens.available())
    {
      HUSKYLENSResult result = huskylens.read();
      //printResult(result);
      //save the result in centerX[n]
      centerX[n] = result.xCenter;
      centerY[n] = result.yCenter;
      n++;
    }
    //sort block by CenterX - the newest one
    int minVal = centerX[0];
    int minIndex = 0;
    for (int i = 0; i < n; i++) {
      if (centerX[i] < minVal) {
        minVal = centerX[i];
        minIndex = i;
      }
    }
    //compared with DefultX
    checkIndex = n - 1;
    getNotedY(checkIndex);
    /////////////////

    int area = abs(centerY[minIndex] - correctNote);
    if (area >= 15) {
      password = true;
    }
    else {
      password = false;
    }

    /////////////////
    changeCoordinate(minIndex);
    ////////////////////////////////////////////////////////////////////////
    ///////this part is to communicate with robot
    if (password == true) {
      if (checkIndex > targetIndex) {
        targetIndex = checkIndex;
        passData2Py();
      }
      else {
        passPause2Py();
      }
    } else {
      if (checkIndex > targetIndex) {
        targetIndex = checkIndex;
        int sound = targetIndex + 10;
        passSound2Py(sound);
      }
      else {
        passPause2Py();
      }

    }
  }//the end of else
}//the end of loop


////functions
///////////////////////////////////////////////////////////////////////////////////////////////////////
//function to get the rightest block and it's index
//function to compare the rightest position

//function to print the current block data
void printResult(HUSKYLENSResult result) {
  if (result.command == COMMAND_RETURN_BLOCK) {
    Serial.println(String() + F("Block:xCenter=") + result.xCenter + F(",yCenter=") + result.yCenter + F(",width=") + result.width + F(",height=") + result.height + F(",ID=") + result.ID);
  }
  else if (result.command == COMMAND_RETURN_ARROW) {
    Serial.println(String() + F("Arrow:xOrigin=") + result.xOrigin + F(",yOrigin=") + result.yOrigin + F(",xTarget=") + result.xTarget + F(",yTarget=") + result.yTarget + F(",ID=") + result.ID);
  }
  else {
    Serial.println("Object unknown!");
  }
}
//function to get the correct Y of No.X
void getNotedY (int x) {
  int array[] = {160, 140, 60, 200}; //the block is 320 * 240, the first one is beginner
  correctNote = array[x];
}
//function to change coordinate
void changeCoordinate(int i) {
  targetY = map(centerX[i], 0, 320, 190, -190); //change to real coordinate
  targetX = map(centerY[i], 0, 240, 473, 190);
}
//function to sending data to python
void passData2Py() {
  Serial.print(targetIndex);
  Serial.print(",");
  Serial.print(targetX);
  Serial.print(",");
  Serial.println(targetY);
}
void passPause2Py() {
  Serial.print(9);
  Serial.print(",");
  Serial.print(9);
  Serial.print(",");
  Serial.println(9);
}
void passSound2Py(int sound) {
  Serial.print(sound);
  Serial.print(",");
  Serial.print(9);
  Serial.print(",");
  Serial.println(9);
}
