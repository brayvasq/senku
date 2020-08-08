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
      boards: [],
      run: 'Run',
      steps: 0,
      solutionSteps: 0
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
    this.setState({ run: "Processing...", boards: [], steps: 0, solutionSteps: 0 })

    const data = {
      algorithm: this.state.algorithm,
      initial: this.initial
    }

    axios({
      method: 'post',
      url: 'http://localhost:8000/api/game/',
      data: data
    }).then(resp => {
      // console.log(resp)
      this.setState(
        { 
          boards: resp["data"]["result"], 
          run: "Run",
          steps: resp["data"]["steps"],
          solutionSteps: resp["data"]["solution_steps"]
        }
      );
    })
  }

  render(){
    return(
      <div className="container">
        <div className="header">Senku</div>
        <div className="boards">
          <Board value={this.initial}></Board>
          {this.state.boards.map((board) => {
            return(
              <Board value={board}></Board>
            );
          })}
        </div>
        <div className="info">
          <div>
            <select onChange={this.handleChangeInput}>
                <option value="bfs">BFS - Breadth First Search</option>
                <option value="dfs">DFS - Depth First Search</option>
                <option value="greedy">Greedy</option>
                <option value="a_star">A Star</option>
            </select>
          </div>
          <div>
            <input type="submit" value={this.state.run} onClick={this.getBoards}/>
          </div>
          <div>
            <table>
              <tbody>
                <tr>
                  <td className="title">Steps:</td>
                  <td className="value">{this.state.steps}</td>
                </tr>
                <tr>
                  <td className="title">Solution steps:</td>
                  <td className="value">{this.state.solutionSteps}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }
}

export default Game;
