import React, {Component} from 'react';
import './Cell.css';

class Cell extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <button className="cell">
                {this.props.num}
            </button>
        )
    }
}

export default Cell;
