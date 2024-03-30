import { Row, Col } from 'react-bootstrap'

import { news } from '../news'

function NewsScreen() {
  return (
    <div>
      <h1>Новини</h1>
      <Row>
        {news.map(newsItem => (
          <Col key={newsItem._id} sm={12} md={6}>
            <h3>{newsItem.title}</h3>
          </Col>
        ))}
      </Row>
    </div>
  )
}

export default NewsScreen
