import { combineReducers } from 'redux';
import qrcodeReducer from './qrcode';
// import PostReducer from './reducer_post';
// import { reducer as formReducer } from 'redux-form';

const rootReducer = combineReducers({
    qrcode: qrcodeReducer;
});

export default rootReducer;
