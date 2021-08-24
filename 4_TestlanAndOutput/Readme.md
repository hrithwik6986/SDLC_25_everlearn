## Test Plan and Output

### High Level Test Plan

 ID  | Description  | Expected Input | Expected Output | Status | Test Type
 --- | ------------ | -------------- | --------------- | ------ | ---------
 HR01 | System Compatability | System requirements | Environment ready | PASS | Scenario 
 HR02 | Random word Selected | Key press | A Word selected to guess from a set of words |  | Technical
 HR03 | User chooses a letter | Input letter | user guessed a letter |  | Technical
 HR04 | User wins if all letters are guessed correctly | Input letter |  'User wins' message shown |  | Technical
 HR05 | User loses if all letters are not guessed correctly after some attempts | Input letter | 'User loses' message shown |  | Technical
 HR06 | Rules for quiz | Key press | Quiz rules displayed to the user |  | Technical
 HR07 | Status of question answered | User option | Correct or Incorrect answer with amount displayed |  | Technical
 HR08 | Check if quiz game over | User option | 'Game finished' message shown with final amount obtained |  | Technical
 HR09 | Grid for TicTacToe | Key press | Grid displayed for the game |  | Technical
 HR10 | User and Computer play | Key press | User and computer play alternatively with X and O |  | Technical
 HR11 | Tictactoe Game complete | Key press | Game ends with the winner name displayed |  | Technical
 HR12 | Snake GUI | Key press | GUI opened properly |  | Technical
 HR13 | Snake movement | Key press | Snake moved in correct direction |  | Technical
 HR14 | Snake growth | Key press | Length of snake increased when hits the cube |  | Technical
 HR15 | Snake game complete | Key press | 'Game completed' message with the score shown |  | Technical

 ### Low Level Test Plan

  ID  | HLT ID | Description  | Expected Input | Expected Output | Status | Type
  --- | ------ | ------------ | -------------- | --------------- | ------ | ---------
  LR01 | HR01 | Requirements setup | System setup | Setup Success | PASS | Scenario 
  LR02 | HR03 | Choose correct letter | Input letter | Part of word formed with the letter |  | Requirement
  LR03 | HR03 | Choose wrong letter | Input letter | A part of hangman formed |  | Requirement
  LR04 | HR05 | Check number of attempts | Key press | Maximum number of attempts reached and hangman formed completely |  | Requirement
  LR05 | HR05 | User play again | Key press | User continue or quit playing |  | Requirement
  LR06 | HR06 | Rules for quiz | Key press | User accepts or rejects the rules |  | Requirement
  LR07 | HR07 | Quiz question status | User option | Displays correct or incorrect option with scores |  | Requirement
  LR08 | HR07 | Lives status | User option | Displays the lives and helpline left |  | Requirement 
  LR09 | HR08 | All lives are over | Key press | 'Game over' message with final amount scored |  | Requirement
  LR10 | HR08 | All questions are done | Key press | 'Game over' message with final amount scored |  | Requirement
  LR11 | HR09 | Tictactoe grid  designed | Key press | A empty 3x3 grid created for tictactoe |  | Requirement
  LR12 | HR09 | Grid update | key press | The grid updated and displayed after every move |  | Requirement
  LR13 | HR10 | User play | Number from positions 1-9 which is remaining  | X placed at user given position |  | Requirement
  LR14 | HR10 | Computer play | Number from positions 1-9 which is remaining  | O placed at selected position |  | Requirement
  LR15 | HR11 | User wins | Key press | 'User won' message shown |  | Requirement
  LR16 | HR11 | Computer wins | Key press | 'Computer won' message shown |  | Requirement
  LR17 | HR12 | GUI design | Length and width for the frame | GUI frame created |  | Requirement
  LR18 | HR13 | Snake head coordinate change | Arrow keys for movement | Snake movement in the specified direction |  | Requirement
  LR19 | HR15 | Snake hits itself | Key press | 'Game over' message with scores |  | Requirement
  LR20 | HR15 | Snake hits wall | Key press | 'Game over' message with scores |  | Requirement
  LR21 | HR16 | Snake reaches maximum length | Key press | 'User wins' message |  | Requirement