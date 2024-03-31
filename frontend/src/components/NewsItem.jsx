import { Card } from 'react-bootstrap'

function NewsItem({ newsItem }) {
  return (
    <Card className="h-100 text-light">
      <Card.Img src={`/news-photos/${newsItem.url}`} />
      <Card.Body className="">
        <Card.Title className="fw-bold">{newsItem.title}</Card.Title>
        <Card.Text>{newsItem.text}</Card.Text>
      </Card.Body>
    </Card>
  )
}

export default NewsItem
