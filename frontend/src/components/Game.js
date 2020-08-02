import React, { Component } from 'react';
import './Game.css';
import Board from './Board';

/**
 * Component that will show boards games
 */
class Game extends Component {
  /**
   * Component constructor where props and states are defined.
   * Here we can define a state list and bind methods to the component.
   * @param props component properties
   */
  constructor(props){
    super(props);

    this.state = {
      boards: []
    }

    this.getBoards = this.getBoards.bind(this);
  }

  /**
   * Gets the solution from backend service
   */
  getBoards() {
    const boards = [
        [
          ["_","_","_","_","1","_","_","_","_"],
          ["_","_","_","1","_","1","_","_","_"],
          ["_","_","1","_","1","_","1","_","_"],
          ["_","1","_","1","_","1","_","1","_"],
          ["0","_","1","_","1","_","1","_","1"]
        ]
    ]

    this.setState({ boards: boards })
  }

  render(){
    const boards = [
      [
        ["_","_","_","_","1","_","_","_","_"],
        ["_","_","_","1","_","1","_","_","_"],
        ["_","_","1","_","1","_","1","_","_"],
        ["_","1","_","1","_","1","_","1","_"],
        ["0","_","1","_","1","_","1","_","1"]
      ]
    ]

    return(
      <div>
        <div className="boards">
          <Board value={boards}></Board>
          <Board value={boards}></Board>
        </div>
        <div className="info">
          Info!
        </div>
      </div>
    );
  }
}

export default Game;
