import axios from 'axios';

export const FETCH_QRCODE = 'FETCH_QRCODE';

const ROOT_URL = 'https://2oc3yo4sj9.execute-api.us-west-2.amazonaws.com/dev';

export function fetchCode() {
    const request = axios.get(`${ROOT_URL}/api/challenge`);

    return {
        type: FETCH_QRCODE,
        payload: request
    }
}

//________________________________________________________________________________
// export function fetchPosts() {
//     const request = axios.get(`${ROOT_URL}/posts${API_KEY}`);

//     return {
//         type: FETCH_POSTS,
//         payload: request
//     };
// }

// export function createPost(props) {
//     const request = axios.post(`${ROOT_URL}/posts${API_KEY}`, props);

//     return {
//         type: CREATE_POST,
//         payload: request
//     };
// }

// export function fetchPost(id) {
//     const request = axios.get(`${ROOT_URL}/posts/${id}${API_KEY}`);

//     return {
//         type: FETCH_POST,
//         payload: request
//     };
// }

// export function deletePost(id) {
//     const request = axios.delete(`${ROOT_URL}/posts/${id}${API_KEY}`);

//     return {
//         type: DELETE_POST,
//         payload: request
//     };
// }

