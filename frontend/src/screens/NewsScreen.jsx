import { Row, Col } from 'react-bootstrap'

import { news } from '../news'
import NewsItem from '../components/NewsItem'

function NewsScreen() {
  return (
    <div>
      <h1>Новини</h1>
      <Row className="row-gap-4 py-3">
        {news.map(newsItem => (
          <Col key={newsItem._id} sm={12} md={6} lg={4}>
            <NewsItem newsItem={newsItem} />
          </Col>
        ))}
      </Row>
    </div>
  )
}

export default NewsScreen

