import React, { Component } from 'react';
import './Board.css';
import Cell from './Cell';

class Board extends Component {
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
                            num++;
                            return <tr> {
                                board.map( (col) => {
                                    num++;
                                    return <Cell num={num}/>
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
