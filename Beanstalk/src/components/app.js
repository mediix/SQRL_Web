import React, { Component } from 'react';

export default class App extends Component {
    render() {
        return (
            <div>
                <h3>HELLO FROM REACT</h3>
                {this.props.children}
            </div>
        );
    }
}
