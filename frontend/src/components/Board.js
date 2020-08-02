import React, { Component } from 'react';
import './Board.css';
import Square from './Square';

class Board extends Component {
    constructor(props) {
        super(props);

        this.state = {
            board: []
        }
    }

    renderSquare(i) {
        return <Square value={i} />;
    }

    render() {
        /*const board = this.props.board.map((list) => {
            list.map((square) => {
                this.renderSquare(square);
            });
        });*/
        console.log(this.props.value);
        return (
            <div className="board">
                {this.props.value.map((row) => {
                    return (
                        <div className="row">
                            {row.map((square) => {
                                return (
                                    <div className="item">
                                        {this.renderSquare(square)}
                                    </div>
                                );
                            })}
                        </div>
                    );
                })}
            </div>
        );
    }
}

export default Board;
