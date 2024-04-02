import { Card, Col, Row } from 'react-bootstrap'

function UserItem({ userItem, setModalShow, setUserClicked }) {
  const fullName = `${userItem.first_name} ${userItem.last_name} ${userItem.fathers_name}`
  const lastPlotIdx = userItem.land_plot.length - 1

  const LandPlots = userItem.land_plot.map((item, idx) => (
    <span key={idx}>{item.number}{idx !== lastPlotIdx ? ", " : ""}</span>
  ))

  const handleCardClick = e => {
    setUserClicked({
      userItem: userItem,
      fullName: fullName,
      landPlots: LandPlots,
    })
    setModalShow(true)
  }

  return (
    <Card onClick={handleCardClick}>
      <Row className="g-0">
        <Col xs={4}>
          <Card.Img src={`/users-photos/${userItem.photo}`} />
        </Col>
        <Col>
          <Card.Body className="p-2 ps-3">
            <Card.Title className="fw-bold fs-4">{fullName}</Card.Title>
            <Card.Subtitle className="pt-1 fs-4">діл.: {LandPlots}</Card.Subtitle>
          </Card.Body>
        </Col>
      </Row>
    </Card>
  )
}

export default UserItem
