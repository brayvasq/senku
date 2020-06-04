import React, {Component} from 'react';
import './Game.css';
import Board from './Board';

class Game extends Component {
  constructor(props){
    super(props)
  }

  render(){
    return(
      <div>
        <h1>Hello World!</h1>
        <Board></Board>
      </div>
    );
  }
}

export default Game;
