import { combineReducers } from 'redux';
import PostReducer from './reducer_post';

const rootReducer = combineReducers({
    // posts: PostReducer,
    qrcode: PostReducer
});

export default rootReducer;
