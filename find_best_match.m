% Find best match
function best_x = find_best_match(patch, strip)
    % TODO: Find patch in strip and return column index (x value) of topleft corner
    min_diff=Inf;
    best_x=0;
    size_strip=size(strip);
    size_patch=size(patch);
    for x = 1:(size_strip(2) - size_patch(2) + 1)
        other_patch=strip(:,x:(x+size_patch(2)-1));
        diff=patch-other_patch;
        diff_sq=sumsqr(diff(:));
        if diff_sq<min_diff
            min_diff=diff_sq;
            best_x=x;
        end
    end% placeholder
end