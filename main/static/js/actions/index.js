import fetch from 'isomorphic-fetch'

export const REQUEST_POSTS = 'REQUEST_POSTS'
export const RECEIVE_POSTS = 'RECEIVE_POSTS'
export const INVALIDATE_HN = 'INVALIDATE_HN'


export function invalidateHN(hn) {
  return {
    type: INVALIDATE_HN,
    hn
  }
}

function requestPosts(hn) {
  return {
    type: REQUEST_POSTS,
    hn
  }
}

function receivePosts(hn, json) {
  return {
    type: RECEIVE_POSTS,
    hn: hn,
    posts: json.data.posts,
    receivedAt: Date.now()
  }
}

function fetchPosts(hn) {
  return dispatch => {
    dispatch(requestPosts(hn))
    return fetch(`/api.json`)
      .then(response => response.json())
      .then(json => dispatch(receivePosts(hn, json)))
  }
}

function shouldFetchPosts(state, hn) {
  const posts = state.postsByHN[hn]
  if (!posts) {
    return true
  }
  if (posts.isFetching) {
    return false
  }
  return posts.didInvalidate
}

export function fetchPostsIfNeeded(hn) {
  return (dispatch, getState) => {
    if (shouldFetchPosts(getState(), hn)) {
      return dispatch(fetchPosts(hn))
    }
  }
}
