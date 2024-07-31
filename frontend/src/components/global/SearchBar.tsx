import React, { useState } from 'react';
import { FormControl } from 'react-bootstrap';

const SearchBar: React.FC = () => {
    const [query, setQuery] = useState<string>('');

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    };

    const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    const handleSearch = () => {
        // Perform the search or navigate to a search results page
        console.log('Search query:', query);
    };

    return (
        <FormControl
            type="text"
            placeholder="Search"
            value={query}
            onChange={handleChange}
            onKeyDown={handleKeyDown} // Handle Enter key
            style={{ width: '100%' }} // Adjust the width as needed
            className="me-2" // Add some margin to the right
        />
    );
};

export default SearchBar;

