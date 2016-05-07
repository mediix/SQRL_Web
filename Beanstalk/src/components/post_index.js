import React, { Component } from 'react';
import { connect } from 'react-redux';
import { fetchCode } from '../actions/index';
import { Link } from 'react-router';

class PostsIndex extends Component {
    componentWillMount() {
        // this.props.fetchPosts();
        console.log('Component Renders Here.');
        return (
            <div>
                <h3>HELLO FROM REACT</h3>
            </div>
        );
    }

    render() {
        return (
            <div>
                <div className="text-xs-right">
                    <Link to="posts/new" className="btn btn-primary">
                        <span className="glyphicon glyphicon-qrcode" aria-hidden="true"></span>
                        Request QRCode
                    </Link>
                </div>
                <h3>QRCode</h3>
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {posts: state.posts.all};
}


// export default connect(mapStateToProps, {fetchPosts})(PostsIndex);
export default connect(mapStateToProps, {fetchCode})(PostsIndex);
