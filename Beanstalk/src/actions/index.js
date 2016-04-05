import axios from 'axios';
import {FETCH_QRCODE} from './types';

const ROOT_URL = 'https://2oc3yo4sj9.execute-api.us-west-2.amazonaws.com/dev';

export function fetchCode(id) {
    const request = axios.get(`${ROOT_URL}/api/challenge`);

    return {
        type: FETCH_QRCODE,
        payload: request
    }
}

// export function fetchPosts() {
//     const request = axios.get(`${ROOT_URL}/api/challenge`);

//     return {
//         type: FETCH_POSTS,
//         payload: request
//     };
// }

// export function createPost(props) {
//     const request = axios.get(`${ROOT_URL}/api/challenge`);

//     return {
//         type: CREATE_POST,
//         payload: request
//     };
// }

// export function fetchPost(id) {
//     const request = axios.get(`${ROOT_URL}/api/challenge`);

//     return {
//         type: FETCH_POST,
//         payload: request
//     };
// }

// export function deletePost(id) {
//     const request = axios.get(`${ROOT_URL}/api/challenge`);

//     return {
//         type: DELETE_POST,
//         payload: request
//     };
// }
