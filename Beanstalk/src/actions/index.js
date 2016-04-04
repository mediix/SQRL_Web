import axios from 'axios';

export const FETCH_POSTS = 'FETCH_POSTS';
export const CREATE_POST = 'CREATE_POST';
export const FETCH_POST = 'FETCH_POST';
export const DELETE_POST = 'DELETE_POST';

const ROOT_URL = 'https://2oc3yo4sj9.execute-api.us-west-2.amazonaws.com/dev';
const API_KEY = '?user=mehdix';

export function fetchPosts() {
    const request = axios.get(`${ROOT_URL}/api/challenge${API_KEY}`);

    return {
        type: FETCH_POSTS,
        payload: request
    };
}

export function createPost(props) {
    const request = axios.get(`${ROOT_URL}/api/challenge${API_KEY}`);

    return {
        type: CREATE_POST,
        payload: request
    };
}

export function fetchPost(id) {
    const request = axios.get(`${ROOT_URL}/api/challenge${API_KEY}`);

    return {
        type: FETCH_POST,
        payload: request
    };
}

export function deletePost(id) {
    const request = axios.get(`${ROOT_URL}/api/challenge${API_KEY}`);

    return {
        type: DELETE_POST,
        payload: request
    };
}
