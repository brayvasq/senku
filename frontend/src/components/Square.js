import React, {Component} from 'react';
import './Square.css';

class Square extends Component
{
    constructor(props)
    {
        super(props);
    }

    render(){
        return(
            <button className="square">
                {this.props.value}
            </button>
        );
    }
}

export default Square;
