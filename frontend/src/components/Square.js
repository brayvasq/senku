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
            <button className={this.props.value === '_' ? 'empty-square' : 'value-square'}>
                {this.props.value === '_' ? '' : this.props.value}
            </button>
        );
    }
}

export default Square;
