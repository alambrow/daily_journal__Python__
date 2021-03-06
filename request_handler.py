from entries.request import delete_entry, find_entry_by_keyword, get_entry_by_id, get_all_entries, create_journal_entry, update_entry
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        """Parses url string
        """
        path_params = path.split("/")
        resource = path_params[1]
        if "?" in resource:
            resource = resource.split("?")[0]  
            param = resource.split("?")[1]  
            pair = param.split("=")  
            key = pair[0]  
            value = pair[1]  
            return ( resource, key, value )
        else:
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/
            return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response
        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """performs GET function"""
        self._set_headers(200)
        response = {}  # Default response
        parsed_url = self.parse_url(self.path)

        if len(parsed_url) == 2:
            (resource, id) = parsed_url
            if resource == "entries":
                if id is not None:
                    response = f"{get_entry_by_id(id)}"
                else:
                    response = f"{get_all_entries()}"
        elif len(parsed_url) == 3:
            ( resource, key, value ) = parsed_url
            if key == "q" and resource == "entries":
                # pass in value to SQL database search
                response = f"{find_entry_by_keyword(value)}"
        
        self.wfile.write(response.encode())

    # # Here's a method on the class that overrides the parent's method.
    # # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server
        """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initializations
        new_entry = None
        if resource == "entries":
            new_entry = create_journal_entry(post_body)
            self.wfile.write(f"{new_entry}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False
        if resource == "entries":
            success = update_entry(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())


    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()