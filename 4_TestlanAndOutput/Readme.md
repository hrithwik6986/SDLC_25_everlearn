## Test Plan and Output

### Hangman

| ID  | Description  | Expected Input  | Expected_Output  |
| --- | ------------ | --------- | ------- |
| HR01| Random string is taken | - | String is picked from the set of string randomly |
| HR02| guessing of the letters | input letter | only letter is accepted |
| HR03| if letter not in string | input letter | hangman each part is seen for each wrong letter |
| HR04| if letter in string | input letter | letter is filled in its place in the string |
| HR05| guessing the letters in the string | input number | display message to give letter as input |
| HR06| guessing the letters in the string | input more than one letter | display message to give letter as input |
| HR07| guessing the letters in the string | input any other special characters | display message to give letter as input |
| HR08| if the hangman is formed | yes or no to play again | if yes game is started again else exit from game and return to main|


