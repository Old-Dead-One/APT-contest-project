import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";

interface LeftFeedProps {
    chapterList: string;
}

const LeftFeed: React.FC<LeftFeedProps> = (props) => {
    return (
        <Container>
            <Row>
                <Col>
                    <Card>
                        <Card.Body>
                            {props.chapterList}
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
}

export default LeftFeed;