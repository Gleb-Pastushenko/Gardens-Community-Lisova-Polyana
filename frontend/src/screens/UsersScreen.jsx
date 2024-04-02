import { Col, Row } from "react-bootstrap"

import UserItem from '../components/UserItem'
import { users } from '../users'

function UsersScreen() {
  return (
    <div>
      <h2>Члени товариства</h2>

      <Row className="row-gap-4 py-3">
        {users.map(user => (
          <Col key={user._id} sm={12} md={6} xl={4}>
            <UserItem userItem={user} />
          </Col>
        ))}
      </Row>
    </div>
  )
}

export default UsersScreen
