import React, {Component} from 'react';
import './Cell.css';

class Cell extends Component {
    constructor(props){
        super(props);
    }

    render() {
        var handler = this.props.handler;
        return (
            <button className="cell" onClick = {() => handler(this.props.num)}>
                {this.props.num}
            </button>
        )
    }
}

export default Cell;
