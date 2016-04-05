import {FETCH_QRCODE} from '../actions/types';

export default function(state = [], action) {
    switch(action.type) {
        case FETCH_QRCODE:
            return [...state, ...action.payload];
    }

    return state;
}
