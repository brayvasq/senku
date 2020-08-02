import React, { Component } from 'react';
import './Game.css';
import Board from './Board';
import axios from 'axios';

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

    this.initial = [
      ["_","_","_","_","1","_","_","_","_"],
      ["_","_","_","1","_","1","_","_","_"],
      ["_","_","1","_","1","_","1","_","_"],
      ["_","1","_","1","_","1","_","1","_"],
      ["0","_","1","_","1","_","1","_","1"]
    ]

    this.state = {
      algorithm: 'bfs',
      boards: []
    }

    this.getBoards = this.getBoards.bind(this);
    this.handleChangeInput = this.handleChangeInput.bind(this);
  }

  handleChangeInput(event) {
    this.setState({algorithm: event.target.value})
  }

  /**
   * Gets the solution from backend service
   */
  getBoards() {
    const data = {
      algorithm: this.state.algorithm,
      initial: this.initial
    }

    axios({
      method: 'post',
      url: 'http://localhost:8000/api/game/',
      data: data
    }).then(resp => {
      console.log(resp)
      this.setState({ boards: resp["data"] })
    })
  }

  render(){
    return(
      <div>
        <div className="boards">
          <Board value={this.initial}></Board>
          {this.state.boards.map((board) => {
            return(
              <Board value={board}></Board>
            );
          })}
        </div>
        <div className="info">
          <input className="input is-primary" type="text" placeholder="Primary input" value={this.state.algorithm} onChange={this.handleChangeInput}/>
          <input type="submit" value="Run" onClick={this.getBoards}/>
        </div>
      </div>
    );
  }
}

export default Game;
