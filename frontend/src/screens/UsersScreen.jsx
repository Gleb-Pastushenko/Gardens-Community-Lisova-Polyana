import { Col, Row } from "react-bootstrap"
import { useState } from 'react'

import UserItem from '../components/UserItem'
import UserDetailModal from "../components/UserDetailsModal"
import { users } from '../users'

function UsersScreen() {
  const [modalShow, setModalShow] = useState(false)
  const [userClicked, setUserClicked] = useState({})

  return (
    <div>
      <h2>Члени товариства</h2>

      <Row className="row-gap-4 py-3">
        {users.map(user => (
          <Col key={user._id} sm={12} md={6} xl={4}>
            <UserItem
              userItem={user}
              setModalShow={setModalShow}
              setUserClicked={setUserClicked}
            />
          </Col>
        ))}
      </Row>

      <UserDetailModal show={modalShow} onHide={() => setModalShow(false)} user={userClicked} />
    </div>
  )
}

export default UsersScreen
