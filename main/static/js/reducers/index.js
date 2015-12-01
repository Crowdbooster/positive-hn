import { combineReducers } from 'redux'
import {
  INVALIDATE_HN,
  REQUEST_POSTS, RECEIVE_POSTS
} from '../actions'


function posts(state = {
  isFetching: false,
  didInvalidate: false,
  items: []
}, action) {
  switch (action.type) {
    case INVALIDATE_HN:
      return Object.assign({}, state, {
        didInvalidate: true
      })
    case REQUEST_POSTS:
      return Object.assign({}, state, {
        isFetching: true,
        didInvalidate: false
      })
    case RECEIVE_POSTS:
      return Object.assign({}, state, {
        isFetching: false,
        didInvalidate: false,
        items: action.posts,
        lastUpdated: action.receivedAt
      })
    default:
      return state
  }
}

function postsByHN(state = { }, action) {
  switch (action.type) {
    case INVALIDATE_HN:
    case RECEIVE_POSTS:
    case REQUEST_POSTS:
      return Object.assign({}, state, {
        [action.hn]: posts(state[action.hn], action)
      })
    default:
      return state
  }
}

const rootReducer = combineReducers({
  postsByHN,
})

export default rootReducer
