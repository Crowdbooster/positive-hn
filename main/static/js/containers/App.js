import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { selectHN, fetchPostsIfNeeded, invalidateHN } from '../actions'
import FlipButton from '../components/FlipButton'
import Posts from '../components/Posts'

class App extends Component {
  constructor(props) {
    super(props)
    this.handleChange = this.handleChange.bind(this)
    this.handleRefreshClick = this.handleRefreshClick.bind(this)
  }

  componentDidMount() {
    const { dispatch, selectedHN } = this.props
    dispatch(fetchPostsIfNeeded(selectedHN))
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.selectedHN !== this.props.selectedHN) {
      const { dispatch, selectedHN } = nextProps
      dispatch(fetchPostsIfNeeded(selectedHN))
    }
  }

  handleChange(nextHN) {
    this.props.dispatch(selectHN(nextHN))
  }

  handleRefreshClick(e) {
    e.preventDefault()

    const { dispatch, selectedHN } = this.props
    dispatch(invalidateHN(selectedHN))
    dispatch(fetchPostsIfNeeded(selectedHN))
  }

  render() {
    const { selectedHN, posts, isFetching, lastUpdated } = this.props
    return (
      <div>
        <FlipButton value={selectedHN}
            onSubmit={this.handleChange}
        <p>
          {lastUpdated &&
            <span>
              Last updated at {new Date(lastUpdated).toLocaleTimeString()}.
              {' '}
            </span>
          }
          {!isFetching &&
            <a href="#"
               onClick={this.handleRefreshClick}>
              Refresh
            </a>
          }
        </p>
        {isFetching && posts.length === 0 &&
          <h3>Loading...</h3>
        }
        {!isFetching && posts.length === 0 &&
          <h3>No Posts</h3>
        }
        {posts.length > 0 &&
          <div style={{ opacity: isFetching ? 0.5 : 1 }}>
            <Posts posts={posts} />
          </div>
        }
      </div>
    )
  }
}

App.propTypes = {
  selectedHN: PropTypes.string.isRequired,
  posts: PropTypes.array.isRequired,
  isFetching: PropTypes.bool.isRequired,
  lastUpdated: PropTypes.number,
  dispatch: PropTypes.func.isRequired
}

function mapStateToProps(state) {
  const { selectedHN, postsByHN } = state
  const {
    isFetching,
    lastUpdated,
    items: posts
  } = postsByHN[selectedHN] || {
    isFetching: true,
    items: []
  }

  return {
    selectedHN,
    posts,
    isFetching,
    lastUpdated
  }
}

export default connect(mapStateToProps)(App)
