import { FETCH_QRCODE } from '../actions/index';

// const INITIAL_STATE = { all: [], post: null, qrcode: null };
const INITIAL_STATE = { qrcode: null };

export default function(state=INITIAL_STATE, action) {
    switch(action.type) {
        case FETCH_QRCODE:
            return { ...state, qrcode: action.payload.data };
        default:
            return state;
    }
}
