import React, { Component } from 'react';
import './Board.css';
import Cell from './Cell';

class Board extends Component {
    constructor(props){
        super(props)
        this.state = {
            origin: -1,
            target: -1
        };

        this.handler = this.handler.bind(this);
    }

    componentDidUpdate() {
        console.log("componentDidUpdate fired");
        console.log("STATE", this.state);
    }

    handler(item){
        console.log('Click' + item);
        
        if(this.state.origin === -1){
            this.setState({
                origin: item
            });
        } else if (this.state.target === -1){
            this.setState({
                target: item
            }); 
        } else {
            this.setState({
                origin: -1,
                target: -1
            });
        }
    }

    render(){
        let board = Array(5);
        for (let i = 0; i < 5; i++ ) {
            board[i] = i;
        }
        let num = 0;
        return (
            <div>
                <table>
                    <tbody>
                    {
                        board.map( (row) => {
                            return <tr> {
                                board.map( (col) => {
                                    num++;
                                    return <Cell key={num} num={num} handler = {this.handler}/>
                                })
                            }
                            </tr>
                        })
                    }
                    </tbody>
                </table>
            </div>
        );
    }
}

export default Board;
