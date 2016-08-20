/**
 * Created by milesg on 8/11/16.
 */

var Button = ReactBootstrap.Button;
var Modal = ReactBootstrap.Modal;
var OverlayTrigger = ReactBootstrap.OverlayTrigger;
var Popover = ReactBootstrap.Popover;
var Tooltip = ReactBootstrap.Tooltip;
var Form = ReactBootstrap.Form;
var FormGroup = ReactBootstrap.FormGroup;

class ContactForm extends  React.Component {
    constructor(props){
        super(props);
    }

    render () {
        const popover = (
          <Popover id="modal-popover" title="popover">
            very popover. such engagement
          </Popover>
        );
        const tooltip = (
          <Tooltip id="modal-tooltip">
            wow.
          </Tooltip>
        );

        return (
            <div className="row">
                <div className="col-xs-4 col-xs-offset-4">
                <Modal {...this.props} style={{'margin-top': '10%'}}>
                    <Modal.Header closeButton>
                        <Modal.Title>Contact us</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <form>
                            <div className="form-group">
                                <label htmlFor="email">Your email</label>
                                <input name="email" className="form-control" type="email"/>
                            </div>
                            <div className="form-group">
                                <label name="message" htmlFor="message">Message</label>
                                <textarea name="message" rows="5" className="form-control" type="text"/>
                            </div>
                            <div className="form-group text-center">
                                <button type="submit" className="btn btn-primary">Send!</button>
                            </div>
                        </form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={this.props.onHide}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
                </div>
                </div>
        )
    }
}


class BusinessAreas extends React.Component {
    constructor(props){
        super(props)
    }

    render (){
        return (
            <div className="row">
                <div className="col-md-12">
                    <div className="jumbotron">
                        <div className="well well-lg">
                            <p>
                                Welcome to the about page!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

class Main extends React.Component {

    constructor(props){
        super(props);
        this.successful = false;
        this.state = {view: 'home', serverData: null, showContactForm: false};
    }

    componentDidMount(){
        console.log('Mounted');
        document.getElementById('home-link').addEventListener('click', function(){ this.setState({view: 'home'})}.bind(this));
        document.getElementById('contact-us').addEventListener('click', function(){this.setState({showContactForm: true})}.bind(this));

    }
    componentWillUnmount (){
        console.log('Unmounting');
    }

    componentDidUpdate (){
        console.log('Updated!');
    }

    contactUs (){
        console.log('rendering contact form!');
        var close = () => this.setState({showContactForm: false});


        return(
            <ContactForm show={true} onHide={close}  />
        )

    }

    renderHome() {
        return(
            <div className="well well-md text-center">
                <h3>There's a lot of data out there.</h3>
                <h4>Let's make sense of it.</h4>
                <hr/>
                <button onClick={() => {return this.setState({view: 'areas'})}} className="btn btn-primary" value="Find out more">Find out more.</button>
            </div>
    )
    }

    renderAreas () {
        return (<BusinessAreas/>)
    }

    render () {

        if (this.state.showContactForm) {
            return this.contactUs();
        }

        else if (this.state.view == 'home'){
            return this.renderHome();
        }
        else if (this.state.view == 'areas'){
            return this.renderAreas();
        }


    } // End of main render funct
}

$(document).ready(function(){

    ReactDOM.render(<Main/>, document.getElementById('app'));
});
