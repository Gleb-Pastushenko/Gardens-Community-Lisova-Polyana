import { Modal, Button, Row, Col } from 'react-bootstrap'


function UserDetailModal(props) {
  const { user } = props
  const { fullName, landPlots, userItem } = user

  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          {fullName}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h4 className="mb-3">Ділянки: {landPlots}</h4>
        <Row>
          <Col>Телефон:</Col>
          <Col>{userItem?.phone_number}</Col>
        </Row>
        <Row>
          <Col>Адреса: </Col>
          <Col>{userItem?.home_address}</Col>
        </Row>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  )
}

export default UserDetailModal